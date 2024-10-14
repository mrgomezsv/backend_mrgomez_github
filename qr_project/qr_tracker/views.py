from django.http import JsonResponse
from .models import QRCode
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')



def generate_qr(request):
    if request.method == 'POST':
        # Obtener el texto enviado en la solicitud
        text = request.POST.get('text', '')

        if text:
            # Guardar el QR generado en la base de datos
            qr_code = QRCode.objects.create(text=text)

            # Obtener el número total de códigos QR generados
            qr_count = QRCode.objects.count()

            # Devolver una respuesta JSON con la cuenta actualizada
            return JsonResponse({'message': 'QR generado con éxito', 'qr_count': qr_count})
        else:
            return JsonResponse({'error': 'No se proporcionó ningún texto'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
