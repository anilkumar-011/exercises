import string
from django.db import connection, transaction
from django.db.models import Prefetch
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import PersonSerializer
from rest_framework import viewsets
import random
from django.db.models.signals import post_delete


# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.values()
    serializer_class = PersonSerializer



class Orm1(APIView):

    def get(self, request):
        query = request.GET.dict()
        persons = Person.objects.all()
        for key, value in query.items():
            persons = persons.filter(**{key: value})
        if not persons:
            return Response('Please provide the crt id', 400)
        foriegn_key = persons.first().vehicle_id

        no_queries = len(connection.queries)
        print(foriegn_key)
        return Response({'Number of queries ran': no_queries}, 200)


class Orm2(APIView):
    def get(self, request):
        persons = list(map(lambda x: x + 100, Person.objects.values_list('ID', flat=True)))
        print(persons)
        return Response({101,102,103,104}, 200)


class Orm3(APIView):
    def get(self, request):
        persons = Person.objects.all().values()
        vehicles = Vehicle.objects.all().values()
        response = []
        for i in vehicles:
            count = 0
            for j in persons:
                if j.get('vehicle_id', None) == i.get('id', None): count += 1
            x = {
                "id": i.get('id', None),
                "count_of_related_objects": count,
            }
            response.append(x)
        return Response(response, 200)


class Orm4(APIView):
    def post(self, request):
        def generate_random_string(length):
            characters = string.printable
            random_string = ''.join(random.choice(characters) for _ in range(length))
            return random_string

        l = [Name(text=generate_random_string(20)) for x in range(100000)]
        Name.objects.bulk_create(l)
        # for i in range(100000):
        #     serializer = NameSerializer(data={'text': random.choice(string.ascii_letters)[:20]})
        return Response('Posted successfully', 200)


class Orm5(APIView):
    def post(self, request):
        l = request.data.get("list", None)
        s = Name.objects.all().values_list()
        count = 0
        for i in s:
            for j in l:
                if j in i[1]: count += 1
        return Response(data={"count matched": count, "list": [l, s]}, status=200)


class Orm6(APIView):
    def get(self, request):
        data = X.objects.all()
        ans = []
        for i in data:
            d_list = D.objects.all().filter(x=i)
            b_list = i.b_values()
            x = {
                "id": i.id,
                'X': i.x,
                'a': A.objects.get(pk=i.a_id).a,
                'b': [x.b for x in b_list],
                'c': C.objects.get(pk=i.c_id).c,
                'd': [d.id for d in d_list],

            }
            ans.append(x)
        print(ans)
        return Response('count of database queries the current View ran: ' + str(len(connection.queries)), 200)


class Orm7(APIView):
    def get(self, request):
        data = X.objects.select_related('a', 'c').prefetch_related(
            Prefetch('b', queryset=B.objects.all()),
            Prefetch('d_set', queryset=D.objects.all())
        ).all()
        ans = []
        for i in data:
            x = {
                "id": i.id,
                'X': i.x,
                'a': i.a.a,
                'b': [x.b for x in i._prefetched_objects_cache['b']],
                'c': i.c.c,
                'd': [x.d for x in i._prefetched_objects_cache['d_set']],
            }
            ans.append(x)
        print(ans)
        return Response('number of queries the view ran: ' + str(len(connection.queries)), 200)


class Orm8(APIView):
    def get(self, request):
        ans = {
            'only': [i.id for i in X.objects.only()],
            'values': [i['id'] for i in X.objects.values()],
            'values_list': [i[0] for i in X.objects.values_list()],
            'defer': [i.id for i in X.objects.defer()],
        }
        # print(ans)
        return Response(ans, 200)


class Orm9(APIView):
    def post(self, request):
        data = request.data
        for i in data:
            if 'id' in i:
                try:
                    x = Name.objects.get(pk=i['id'])
                    x.text = i['name']
                    x.save()
                except:
                    return Response('Enter the correct id number', 400)
            else:
                x = Name(text=i['name'])
                x.save()
        return Response('Done bro', 200)


@receiver(post_delete, sender=Name)
def postDelete(sender, instance, **kwargs):
    print('post delete called', instance.id)


class Orm10(APIView):

    @transaction.atomic
    def post(self, request):
        data = request.data
        n = len(data)
        l1, l2 = data[:n // 2], data[n // 2:]
        x = []
        try:

            l1_list = [Name.objects.get(pk=i) for i in l1]
            for i in l1_list:
                x.append(i.delete(post_delete=False))

            l2_list = [Name.objects.get(pk=i) for i in l2]
            for i in l2_list:
                i.delete()

        except Name.DoesNotExist:
            return Response('Enter the correct ID numbers', status=400)

        return Response([l1, l2], 204)


class Orm11b(APIView):
    def get(self, request):
        return Response('count of rows in Names:' + str(len(Name.objects.all())), 200)


class Orm11c(APIView):
    def get(self, request, id):
        query = request.GET.dict()
        data = query.get('data', None)
        if data == 'false': return Response(False, 400)
        try:
            x = Name.objects.get(pk=id)
            return Response({"id": id, "name": x.text}, 200)
        except:
            return Response(False, 404)
