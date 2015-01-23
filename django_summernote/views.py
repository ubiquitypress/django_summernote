from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect
from django_summernote.models import Attachment
from django_summernote.settings import summernote_config
from django.core.urlresolvers import reverse


def editor(request, id):
    url = request.META.get('HTTP_REFERER')
    split_list = url.split('/')

    code = split_list[5]

    kwargs = {
        'id': id,
        'code': code,
    }
    return redirect(reverse('django_summernote-editor-code', kwargs=kwargs))


def editorcode(request, id, code):
    context = {
        'id_src': id,
        'id': id.replace('-', '_'),
        'code': code,
    }
    return render(request, 'django_summernote/widget_iframe_editor.html', context)

def upload_attachment(request):
    referrer_bits = filter(None, request.META.get('HTTP_REFERER').split('/'))
    code = referrer_bits[-1]
    
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST method is allowed')

    if not request.FILES.getlist('files'):
        return HttpResponseBadRequest('No files were requested')

    try:
        attachments = []

        for file in request.FILES.getlist('files'):
            attachment = Attachment()
            attachment.file = file
            attachment.name = file.name
            attachment.code = code

            if file.size > summernote_config['attachment_filesize_limit']:
                return HttpResponseBadRequest(
                    'File size exceeds the limit allowed and cannot be saved'
                )

            attachment.save()
            attachments.append(attachment)

        return render(request, 'django_summernote/upload_attachment.json', {
            'attachments': attachments,
        })
    except IOError:
        return HttpResponseServerError('Failed to save attachment')
