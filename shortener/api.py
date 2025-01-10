from ninja import Router
from .schemas import LinkSchema, UpdateLinkSchema
from .models import Links, Clicks
from django.shortcuts import get_object_or_404, redirect
from io import BytesIO
import base64
import qrcode

shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = link_schema.to_model_data()

    
    if data['token'] and Links.objects.filter(token=data['token']).exists():
        return 409, {'error': 'Token já existe, use outro'}

    link = Links(**data)
    link.save()

    return 200, LinkSchema.from_model(link)

@shortener_router.get('/{token}', response={200: None, 404:dict})
def redirect_link(request, token):
    link = get_object_or_404(Links, token=token, active=True)
    
    if link.expired():
        return 404, {'error': 'Link expirado'}
    
    uniques_clicks = Clicks.objects.filter(link=link).values('ip').distinct().count()
    if link.max_uniques_cliques and uniques_clicks >= link.max_uniques_cliques:
        return 404, {'error': 'Limite de cliques atingido'}
    
    click = Clicks(
        link=link, 
        ip=request.META.get('REMOTE_ADDR')
    )
    click.save()
    
    return redirect(link.redirect_link)

@shortener_router.put('/{link_id}', response={200: UpdateLinkSchema, 404: dict})
def update_link(request, link_id: int, link_schema: UpdateLinkSchema):
    
    link = get_object_or_404(Links, id=link_id)

    
    token = link_schema.dict().get('token')
    if token and Links.objects.filter(token=token).exclude(id=link_id).exists():
        return 409, {'error': 'Token já existe, use outro'}

    
    for field, value in link_schema.dict().items():
        if value is not None:
            setattr(link, field, value)

  
    link.save()

    return 200, UpdateLinkSchema(
        redirect_link=link.redirect_link,
        token=link.token,
        max_uniques_cliques=link.max_uniques_cliques,
        active=link.active,
    )

@shortener_router.get("statistics/{link_id}/", response={200: dict})
def statistics(request, link_id: int):
    link = get_object_or_404(Links, id=link_id)
    uniques_clicks = Clicks.objects.filter(link=link).values('ip').distinct().count()
    total_clicks = Clicks.objects.filter(link=link).values('ip').count()
    return 200, {'uniques_clicks': uniques_clicks, 'total_clicks': total_clicks}

def get_api_url(request, token):
    scheme = request.scheme
    host = request.get_host()
    return f"{scheme}://{host}/api/{token}"

@shortener_router.get("qrcode/{link_id}/", response={200: dict})
def get_qrcode(request, link_id: int):
    link = get_object_or_404(Links, id=link_id)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(get_api_url(request, link.token))
    qr.make(fit=True)

    content = BytesIO()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(content)
    data = base64.b64encode(content.getvalue()).decode('UTF-8')
    return 200, {'content_image': data}