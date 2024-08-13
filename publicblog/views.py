# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile

# @csrf_exempt
# def custom_upload_view(request):
#     if request.method == 'POST':
#         file = request.FILES.get('upload')
#         if file:
#             filename = default_storage.save(file.name, ContentFile(file.read()))
#             file_url = default_storage.url(filename)
#             return JsonResponse({'url': file_url})
#     return JsonResponse({'error': 'Invalid request'}, status=400)
