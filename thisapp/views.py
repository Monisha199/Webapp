from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,JsonResponse,Http404
from .models import User,Group,Group_member,Message

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,GroupSerializer,GroupMemberSerializer

from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request,'home.html')

def Login(request):
    return render(request,"login.html")

class UserList(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    # create user
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    # update user
    def put(self,request,pk):
        updateuser=self.get_object(pk)
        serializer = UserSerializer(updateuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def new_user(request):
    username=request.POST['username']
    user_password=request.POST['user_password']
    check_user= User.objects.filter(name=username).first()

    if not check_user:
        messages.success(request, 'User does not exist, please enter valid username')
        return redirect('/login')

    if check_user:
        if check_user.password_hash==user_password:
            if check_user.role=="admin":
                return redirect('/user')
            return redirect('/chat')
        else:
            messages.success(request, 'Password incorrect')
            return redirect('/login')

class GroupDetails(APIView):
    def get(self,request):
        grouplist= Group.objects.all()
        serializer=GroupSerializer(grouplist,many=True)
        return Response(serializer.data)
    # create group
    def post(self,request):
        serializer=GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GroupUpdate(APIView):

    def get_group(self,pk):
        try:
            return Group.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    # search group
    def get(self,request,pk):
        group=self.get_group(pk)
        serializer=GroupSerializer(group)
        return Response(serializer.data)
    # delete group
    def delete(self,request,pk):
        group=self.get_group(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupMemberInfo(APIView):
    def get_object(self,pk):
        try:
            return Group.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    # update groupname
    def put(self,request,pk):
        user=self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def chatroom(request):
    return render(request,'chatroom.html')

def check_group(request):
    group_name = request.POST['group_name']
    username = request.POST['username']
    

    if Group.objects.filter(name=group_name).exists():
        return redirect('/'+group_name+'/?username='+username)
    else:
        return HttpResponse("Group does not exist")

def group_exists(request,room):
    username = request.GET.get('username')
    room_details = Group.objects.get(name=room)
    return render(request, 'group.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Group.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def Logout(request):
    return render(request,"logout.html")

def exit(request,room):
    return render(request,"logout.html")
