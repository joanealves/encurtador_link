from ninja import Router
from .schemas import LinkSchema
from .models import Links

shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = link_schema.to_model_data()

    
    if data['token'] and Links.objects.filter(token=data['token']).exists():
        return 409, {'error': 'Token já existe, use outro'}

    link = Links(**data)
    link.save()

    return 200, LinkSchema.from_model(link)
