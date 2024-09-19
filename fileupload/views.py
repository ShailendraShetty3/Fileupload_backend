from django.http import JsonResponse
from .models import Reviews
from rest_framework import status, generics, parsers
from django.shortcuts import get_object_or_404
from .serializers import ReviewsSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Reviews List and Create View
class ReviewsListCreateView(generics.GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        book_id = request.query_params.get('book_id', None)
        if book_id:
            reviews = Reviews.objects.filter(book_id=book_id)
        else:
            reviews = Reviews.objects.all()

        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Reviews Detail, Update, and Delete View
class ReviewsDetail(generics.GenericAPIView):
    serializer_class = ReviewsSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_object(self, id):
        try:
            return Reviews.objects.get(pk=id)
        except Reviews.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ReviewsSerializer,
        responses={200: "Success", 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = ReviewsSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ReviewsSerializer,
        responses={200: "Success", 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, id, format=None):
        post = get_object_or_404(Reviews, pk=id)
        serializer = ReviewsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
