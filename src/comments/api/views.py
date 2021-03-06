from django.db.models import Q

from rest_framework.filters import (
        SearchFilter, OrderingFilter,
    )

from rest_framework.generics import (
	    CreateAPIView, 
	    UpdateAPIView, 
	    DestroyAPIView,
	    ListAPIView, 
	    RetrieveAPIView,
	    RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	    AllowAny,
	    IsAuthenticated,
	    IsAdminUser,
	    IsAuthenticatedOrReadOnly,
    )

from posts.api.permissions import IsOwnerOrReadOnly

from posts.api.pagination import (
	    PostLimitOffsetPagination, 
	    PostPageNumberPagination
	)

from comments.models import Comment

from .serializers import (
		CommentSerializer,
		CommentDetailSerializer
    )


# class PostCreateAPIView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'abc'


# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'abc'

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'abc'


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query: 
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__contains=query) |
                Q(user__last_name__contains=query)
                ).distinct()
        return queryset_list