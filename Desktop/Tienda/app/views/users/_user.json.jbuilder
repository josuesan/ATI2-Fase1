json.extract! user, :id, :nombre, :genero, :nacimiento, :username, :created_at, :updated_at
json.url user_url(user, format: :json)
