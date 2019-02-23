class CreateReviewsites < ActiveRecord::Migration[5.2]
  def change
    create_table :reviewsites do |t|
      t.string :url
      t.integer :product_id
      t.datetime :last_crawl
      t.timestamps
    end
  end
end
