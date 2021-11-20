# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Costume(models.Model):
    _name = 'catalog.costume'
    _description = 'Data detail dari setiap busana'

    name = fields.Char(string="Nama", required=True)
    description = fields.Text(string="Deskripsi")
    stock = fields.Integer(string="Stok", required=True)
    image = fields.Image(string="Gambar")

class Reservation(models.Model):
    _name = 'catalog.reservation'
    _description = 'Data pemesanan suatu busana'

    costume_id = fields.Many2many('catalog.costume',string="Id Busana")
    order_datetime = fields.Datetime(string="Tanggal Pemesanan")
    order_identity = fields.Text(string="Pemesan")
    
class User(models.Model):
    _name = 'catalog.user'
    _description = 'Informasi pengguna'

    username = fields.Text(string="Username", required=True)
    password = fields.Text(string="Password" ,required=True)
    role = fields.Text(string="Role" ,required=True)
