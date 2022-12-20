from rest_framework import serializers

from .models import User,Group,Group_member

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('name','id','password_hash','role')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('id','name','creator_id')

class GroupMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group_member
        fields=('id','name','groupname')