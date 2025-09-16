from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')    
    date_availability = fields.Datetime("Data_Availability", copy=False)
    expected_price = fields.Float("Expected price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", index=True)
    living_area = fields.Integer("Living area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden area")
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Orientation is used to separate north and south and east and west")
    state = fields.Selection(
         string='State',
        selection=[('new', 'New'), ('offer', 'Offer'), ('received', 'Received'), ('offer', 'Offer'),        ('accepte', 'Accepte'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="Orientation is used to separate north and south and east and west", 
        required=True, default="new")

    active = fields.Boolean(default=True)
        
    
    
    
    