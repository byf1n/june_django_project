from rest_framework.views import APIView
from rest_framework.response import Response

# # GET
# # POST
# # PUT
# # PATCH
# # DELETE
#
# class UserView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         print(self.request.data)
#         print(self.request.query_params.dict())
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
#
# class UserTestView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('okkk')

users = [
    {'name': 'bobi', 'age': 14},
    {'name': 'alex', 'age': 23},
    {'name': 'oleg', 'age': 43},
    {'name': 'dania', 'age': 13},
]


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        users.append(user)
        return Response(user)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('not found!!!')
        return Response(user)

    def put(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('not found!!!')
        user['name'] = new_user['name']
        user['age'] = new_user['age']

        return Response(user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('asdasdas')
        del users[pk]
        return Response(users[pk])
