class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.string :nombre
      t.string :genero
      t.date :nacimiento
      t.string :username
      t.string :password
      t.string :remember_session
      t.timestamps
    end
  end
end
