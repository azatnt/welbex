from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Car
from main.serailizers import CarSerializer


class Index(APIView):
    def get(self, request):
        return Response("Welcome")


class FilterCar(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 2
        enums = {
            "contains": "icontains",
            "greater": "gte",
            "less": "lte",
            "exact": "exact"
        }

        params = {
            'name': request.GET.get('name'),
            'amount': request.GET.get('amount'),
            'distance': request.GET.get('distance')
        }

        operand = enums[request.GET.get('operand')]

        if (not params['name'] or not params['amount'] or not params['distance']) and not operand:
            return Response({"message": "Заполните все поля!"}, status=status.HTTP_400_BAD_REQUEST)
        cars = Car.objects.filter(*[(f'{key}__{operand}', value) for key, value in params.items() if value]).order_by('id')
        result_page = paginator.paginate_queryset(cars, request)
        serialized_data = CarSerializer(result_page, many=True).data
        return paginator.get_paginated_response(serialized_data)
