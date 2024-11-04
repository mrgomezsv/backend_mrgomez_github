# qr_tracker/views.py
from django.http import JsonResponse
from .models import QRCode
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required
def home(request):
    return render(request, 'home.html')  # Renderiza la plantilla adecuada

class IndexView(TemplateView):
    template_name = 'qr_tracker/index.html'

class CommentsView(TemplateView):
    template_name = 'comments/comments.html'

def generate_qr(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            qr_code = QRCode.objects.create(text=text)
            qr_count = QRCode.objects.count()
            return JsonResponse({'message': 'QR generado con éxito', 'qr_count': qr_count})
        else:
            return JsonResponse({'error': 'No se proporcionó ningún texto'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
