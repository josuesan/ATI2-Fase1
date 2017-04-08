class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable
  
  validates :email, presence: true, uniqueness: true
  validates :username, presence: true, uniqueness: true
  validates :encrypted_password, presence: true
  validates :nombre, presence: true, length: { minimum: 2 }
  validates :nacimiento, presence: true
  validates :genero, presence: true, length: { is: 1 }
  
end
