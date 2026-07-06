from django.shortcuts import get_object_or_404, render

from properties.models import Property

from .models import Inquiry


def contact_agent(request):
    properties = Property.objects.select_related('agent').order_by('-created_at')
    selected_property_id = request.GET.get('property_id', '')
    form_data = {}

    if request.method == 'POST':
        form_data = {
            'name': request.POST.get('name', '').strip(),
            'email': request.POST.get('email', '').strip(),
            'phone': request.POST.get('phone', '').strip(),
            'message': request.POST.get('message', '').strip(),
            'property_id': request.POST.get('property_id', '').strip(),
        }
        selected_property_id = form_data['property_id']

        required_fields = ['name', 'email', 'phone', 'message', 'property_id']
        if not all(form_data[field] for field in required_fields):
            return render(
                request,
                'inquiries/contact-agent.html',
                {
                    'error': 'Please fill in all fields before submitting.',
                    'properties': properties,
                    'selected_property_id': selected_property_id,
                    'form_data': form_data,
                    'active_page': 'contact',
                }
            )

        property_obj = get_object_or_404(properties, pk=form_data['property_id'])
        Inquiry.objects.create(
            property=property_obj,
            name=form_data['name'],
            email=form_data['email'],
            phone=form_data['phone'],
            message=form_data['message'],
        )

        return render(
            request,
            'inquiries/contact-agent.html',
            {
                'properties': properties,
                'selected_property_id': form_data['property_id'],
                'success': 'Your inquiry has been sent to the property agent.',
                'active_page': 'contact',
            }
        )

    return render(
        request,
        'inquiries/contact-agent.html',
        {
            'properties': properties,
            'selected_property_id': selected_property_id,
            'form_data': form_data,
            'active_page': 'contact',
        }
    )
