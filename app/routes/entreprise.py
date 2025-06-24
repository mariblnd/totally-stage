from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Stage, Etudiant, Entreprise
from app import db