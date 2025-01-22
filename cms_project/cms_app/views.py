from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .models import ContentItem
from .serializers import ContentItemSerializer
from django.db.models import Q

class AdminContentItemListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Admin only

    def get(self, request, format=None):
        """
        Admin can view all content
        """
        content_items = ContentItem.objects.all()
        serializer = ContentItemSerializer(content_items, many=True)
        return Response(serializer.data)

class ContentItemListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Get content based on role
        """
        if request.user.role == 'author':
            content_items = ContentItem.objects.filter(author=request.user)
        elif request.user.role == 'admin':
            content_items = ContentItem.objects.all()
        else:
            raise PermissionDenied("You don't have permission to view content.")

        serializer = ContentItemSerializer(content_items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Authors can create content, Admins can also create
        """
        if request.user.role == 'author':
            # The 'author' field should be set automatically to the logged-in user
            request.data['author'] = request.user.id
            serializer = ContentItemSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()  # No need to manually set the 'author' since it's already done
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied("Only authors can create content.")

class ContentItemRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        """
        Retrieve a content item
        """
        try:
            content_item = ContentItem.objects.get(pk=pk)
            if request.user.role == 'author' and content_item.author != request.user:
                raise PermissionDenied("You can only view your own content.")
            serializer = ContentItemSerializer(content_item)
            return Response(serializer.data)
        except ContentItem.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        """
        Update a content item
        """
        try:
            content_item = ContentItem.objects.get(pk=pk)
            if request.user.role == 'author' and content_item.author != request.user:
                raise PermissionDenied("You can only update your own content.")
            # Set the author field automatically to the authenticated user
            request.data['author'] = request.user.id
            serializer = ContentItemSerializer(content_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ContentItem.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        """
        Delete a content item
        """
        try:
            content_item = ContentItem.objects.get(pk=pk)
            if request.user.role == 'author' and content_item.author != request.user:
                raise PermissionDenied("You can only delete your own content.")
            content_item.delete()
            return Response({"detail": "Deleted Successfully"} , status=status.HTTP_204_NO_CONTENT)
        except ContentItem.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class ContentItemSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Search content by matching terms in title, body, summary, and categories.
        """
        search_query = request.query_params.get('q', '').strip()  # Get the search query

        if not search_query:
            return Response(
                {"detail": "Please provide a search query using the 'q' parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Build the query using Q objects
        query = Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(summary__icontains=search_query)

        # Filter content based on the user's role
        if request.user.role == 'author':
            content_items = ContentItem.objects.filter(query, author=request.user)
        elif request.user.role == 'admin':
            content_items = ContentItem.objects.filter(query)
        else:
            return Response(
                {"detail": "You don't have permission to search content."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Serialize and return the results
        serializer = ContentItemSerializer(content_items, many=True)
        return Response(serializer.data)