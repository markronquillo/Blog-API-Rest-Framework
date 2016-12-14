from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	)

from comments.models import Comment


class CommentSerializer(ModelSerializer):
	reply_count = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
			'id',
			'content_type',
			'object_id',
			'parent',
			'content',
			'reply_count'
		]

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0


class CommentChildSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			'id',
			'content',
			'timestamp'
		]


class CommentDetailSerializer(ModelSerializer):
	replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
			'id',
			'content_type',
			'object_id',
			'parent',
			'content',
			'replies',
			'reply_count'
		]

	def get_replies(self, obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data
		return None

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0
