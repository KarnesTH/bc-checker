import { Product } from "../../types";
import ProductCard from "./product-card/ProductCard";

const testData: Product[] = [
  {
    id: 1,
    name: "Portland Zement",
    sku: "PZ-001",
    category: "Zement",
    prices: [
      {
        id: 1,
        price: 12.99,
        unit: "kg",
        vendor: "Bauhaus",
        timestamp: new Date().toISOString(),
      },
      {
        id: 2,
        price: 13.99,
        unit: "kg",
        vendor: "Hornbach",
        timestamp: new Date().toISOString(),
      },
    ],
  },
  {
    id: 2,
    name: "Kalksandstein",
    sku: "KS-001",
    category: "Steine",
    prices: [
      {
        id: 3,
        price: 24.99,
        unit: "Stück",
        vendor: "Hornbach",
        timestamp: new Date().toISOString(),
      },
    ],
  },
];

function ProductGrid() {
  return (
    <div className="p-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {testData.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default ProductGrid;
