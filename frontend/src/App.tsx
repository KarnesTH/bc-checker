import Navbar from "./components/navbar/Navbar";
import ProductGrid from "./components/product-grid/ProductGrid";
import SideBar from "./components/sidebar/Sidebar";

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="flex">
        <SideBar />
        <main className="flex-1">
          <ProductGrid />
        </main>
      </div>
    </div>
  );
}

export default App;
