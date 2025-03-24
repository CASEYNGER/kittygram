from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        # Создаем объект сериализатора и передаем в него данные
        # из POST-запроса
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            # Если полученные данные валидны - сохранем в БД
            serializer.save()
            # Возвращаем JSON со всеми данными нового объекта
            # и статус-код 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не валидны - возвращаем информацию об ошибках
        # и статус-код
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Получаем все объекты модели в случае GET-запроса
    cats = Cat.objects.all()
    # Чтобы сериализатор был готов принять список объектов -
    # передаем именнованный параметр "many=True"
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'POST':
        return Response(
            {
                'message': 'Получены данные',
                'data': request.data
            }
        )
    return Response(
        {
            'message': 'Это был GET-запрос!'
        }
    )
