json.extract! product, :id, :foto, :nombre, :descripcion, :categoria, :precio, :vendido, :created_at, :updated_at
json.url product_url(product, format: :json)
