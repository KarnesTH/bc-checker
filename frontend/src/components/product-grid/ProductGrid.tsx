import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { AppDispatch, RootState } from "../../store";
import { fetchProducts } from "../../store/features/productSlice";
import ProductCard from "./product-card/ProductCard";

function ProductGrid() {
  const dispatch = useDispatch<AppDispatch>();
  const { items, status, error } = useSelector(
    (state: RootState) => state.products,
  );
  const filters = useSelector((state: RootState) => state.filter);

  useEffect(() => {
    if (status === "idle") {
      dispatch(fetchProducts());
    }
  }, [status, dispatch]);

  if (status === "loading") {
    return <div>Loading...</div>;
  }

  if (status === "failed") {
    return <div>Error: {error}</div>;
  }

  const filteredProducts = items.filter((product) => {
    return (
      filters.selectedCategories.includes(product.category) &&
      filters.selectedVendors.includes(product.sku) &&
      product.prices.some(
        (price) =>
          price.price >= filters.priceRange.min &&
          price.price <= filters.priceRange.max,
      )
    );
  });

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {filteredProducts.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}

export default ProductGrid;
