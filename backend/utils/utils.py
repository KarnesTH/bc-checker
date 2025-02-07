def material_to_dict(material):
    """Converts a material object to a dictionary"""
    return {
        'id': material.id,
        'name': material.name,
        'unit': material.unit,
        'prices': [{
            'amount': price.amount,
            'vendor': price.vendor,
            'timestamp': price.timestamp.isoformat()
        } for price in sorted(material.prices, key=lambda p: p.timestamp, reverse=True)]
    }
