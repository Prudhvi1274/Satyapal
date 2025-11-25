# leads/views.py

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from theme.models import ChatbotFlowStep # <--- CMS flow model
import json
from django.db.models import Max 

# Models aur Serializers import karna zaroori hai
from .models import Lead, NewsletterSubscriber
from .serializers import LeadSerializer, NewsletterSubscriberSerializer

# --- 1. Lead ViewSet (Existing) ---
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by("-created_at")
    serializer_class = LeadSerializer

# --- 2. Newsletter Subscriber ViewSet (Existing) ---
class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all().order_by('-subscribed_at')
    serializer_class = NewsletterSubscriberSerializer

# <--- NEW CHATBOT FLOW HANDLER (Replaces chat_with_ai)
@api_view(['POST'])
def chat_flow_handler(request):
    """
    Handles the sequential, CMS-configured chatbot flow. 
    Saves user answers in session until the flow is complete, then generates a Lead.
    """
    try:
        # Get data from request body
        current_field = request.data.get('current_field') # Field the user just answered (e.g., 'name')
        answer = request.data.get('answer')
        
        # Conversation state management using Django session
        flow_data = request.session.get('chatbot_flow_data', {})
        
        # 1. Save the previous answer
        if current_field and answer:
            flow_data[current_field] = answer
            # Mark the session as modified so Django saves it
            request.session['chatbot_flow_data'] = flow_data
            
        # 2. Determine the next step
        if current_field:
            last_step = ChatbotFlowStep.objects.filter(field_to_save=current_field).first()
            last_order = last_step.step_order if last_step else 0
        else:
            last_order = 0
        
        # Find the next step in order
        next_step = ChatbotFlowStep.objects.filter(step_order__gt=last_order).order_by('step_order').first()

        # 3. Check for completion or next question
        if next_step:
            response_data = {
                "next_question": next_step.question_text,
                "next_field": next_step.field_to_save,
                "is_complete": False
            }
        else:
            # 4. Flow is complete: Capture Lead
            lead_name = flow_data.get('name', 'Unknown Chatbot Lead')
            lead_email = flow_data.get('email', 'no-email@chatbot.com')
            
            # Capture the Lead (saves to Lead model with source="chatbot")
            Lead.objects.create(
                name=lead_name,
                email=lead_email,
                phone=flow_data.get('phone', ''),
                service=flow_data.get('service', 'General Inquiry'),
                message=flow_data.get('message', 'Flow completed successfully.'),
                source="chatbot"
            )
            
            # Clean up session data
            if 'chatbot_flow_data' in request.session:
                del request.session['chatbot_flow_data']
            
            response_data = {
                "next_question": f"Thank you, {lead_name}! Your details have been successfully captured. We will contact you shortly.",
                "next_field": None,
                "is_complete": True,
                "action": "lead_captured"
            }
        
        return Response(response_data)
        
    except Exception as e:
        # Log the error and allow the chatbot to restart
        print(f"Chatbot Flow Error: {e}")
        if 'chatbot_flow_data' in request.session:
            del request.session['chatbot_flow_data']
        
        # Fetch the very first question to allow restart
        first_step = ChatbotFlowStep.objects.order_by('step_order').first()
        
        return Response({
            "error": "A system error occurred. Restarting chat...",
            "next_question": first_step.question_text if first_step else "Welcome to XpertAI. How can I assist you?",
            "next_field": first_step.field_to_save if first_step else "name",
            "is_complete": False
        })
# NEW CHATBOT FLOW HANDLER --->