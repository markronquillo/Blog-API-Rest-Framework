from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField
    )

from comments.api.serializers import (
        CommentSerializer,
        CommentDetailSerializer
    )

from comments.models import Comment

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
    lookup_url_kwarg='abc'
    )

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'content',
            'publish',
            'user'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'html',
            'slug',
            'content',
            'publish',
            'image',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        comment_queryset = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(comment_queryset, many=True).data
        return comments
