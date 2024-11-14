from django.shortcuts import render
import json,sys,os
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment
from .forms import TicketForm,CommentForm,UpdateStatusForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from django.contrib.auth.models import User
# Create your views here.
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.Name_of_creator = request.user  # Set the user who created the ticket
            ticket.save()
            return redirect('list_ticket')  # Redirect to the ticket list view after saving
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

def list_ticket(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/list_ticket.html', {'tickets': tickets})

def ticket_detail(request,ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        # Get the new status from the form
        new_status = request.POST.get('status')

        # Update the ticket's status
        if new_status in ['open', 'in_progress', 'closed']:
            ticket.status = new_status
            ticket.save()

        # Redirect back to the ticket detail page to see the updated status
        return redirect('list_ticket')

    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})



@login_required
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    print("ticket is this:", ticket, request)
    if request.method == 'POST':
        print("1")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("2")
            comment = form.save(commit=False)
            comment.ticket = ticket

            if request.user.is_authenticated:
                comment.user = request.user  # Use authenticated user
            else:
                # Ensure the default user exists, if not, create it
                default_user, created = User.objects.get_or_create(username="AnonymousUser")
                comment.user = default_user

            comment.save()

            # Add success message
            messages.success(request, 'Your comment has been added successfully!')

            # Redirect to the ticket detail page
            return redirect('ticket_detail', ticket_id=ticket.id)
        else:
            print("Form errors:", form.errors)  # Print form errors if invalid
    else:
        print("3")
        form = CommentForm()

    print("4")

    return render(request, 'tickets/add_comment.html', {'form': form, 'ticket': ticket})


    # ticket = get_object_or_404(Ticket, id=ticket_id)
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.ticket = ticket
    #         comment.user = request.user  # Assuming user is authenticated
    #         comment.save()
    #         return redirect('tickets/ticket_detail.html', ticket_id=ticket_id)
    # else:
    #     form = CommentForm()
    # return render(request, 'tickets/add_comment.html', {'form': form, 'ticket': ticket})


# views.py
from django.contrib.auth.decorators import user_passes_test

def is_engineer(user):
    # Define logic to check if the user is an engineer
    return user.groups.filter(name='Engineers').exists()

@user_passes_test(is_engineer)
def update_ticket_status(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets/ticket_detail.html', ticket_id=ticket_id)
    else:
        form = UpdateStatusForm(instance=ticket)
    return render(request, 'update_ticket_status.html', {'form': form, 'ticket': ticket})



