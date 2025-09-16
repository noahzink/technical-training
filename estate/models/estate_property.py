from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char('Name', required=True)
    create_date = fields.Datetime("Creation date", readonly=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    data_availability = fields.Datetime("Data_Availability")
    expected_price = fields.Float("Expected price", required=True)
    selling_price = fields.Float("Selling Price")
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

        
    
    
    
    