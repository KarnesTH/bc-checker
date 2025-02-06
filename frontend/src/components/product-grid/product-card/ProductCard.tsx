import { Product } from "../../../types";

interface ProductCardProps {
  product: Product;
}

function ProductCard({ product }: ProductCardProps) {
  const lowestPrice = Math.min(...product.prices.map((p) => p.price));

  return (
    <div className="border rounded-lg p-4 shadow-sm">
      <h3 className="text-lg font-semibold">{product.name}</h3>
      <p className="text-sm text-gray-500">{product.category}</p>
      <div className="mt-4">
        <p className="font-bold">ab {lowestPrice}€</p>
        <div className="mt-2 space-y-1">
          {product.prices.map((price) => (
            <div key={price.id} className="flex justify-between text-sm">
              <span>{price.vendor}</span>
              <span>
                {price.price}€/{price.unit}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default ProductCard;
