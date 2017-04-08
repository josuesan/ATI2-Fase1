Rails.application.routes.draw do
  resources :sessions, only: [:new, :create, :destroy]
  get '/signin',  to: 'sessions#new'
  get '/signout', to: 'sessions#destroy'
  root 'users#index' , as: :user_index

  resources :users
  resources :users do
    resources :comments
  end
  resources :products
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
