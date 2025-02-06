import { useState } from "react";

const categories = ["Zement", "Steine", "Dämmstoffe", "Holz", "Fliesen"];

const vendors = ["Bauhaus", "Hornbach", "OBI", "Hagebau"];

interface PriceRange {
  min: number;
  max: number;
}

function Sidebar() {
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const [selectedVendors, setSelectedVendors] = useState<string[]>([]);
  const [priceRange, setPriceRange] = useState<PriceRange>({
    min: 0,
    max: 100,
  });

  const handleCategoryChange = (category: string) => {
    setSelectedCategories((prev) =>
      prev.includes(category)
        ? prev.filter((c) => c !== category)
        : [...prev, category],
    );
  };

  const handleVendorChange = (vendor: string) => {
    setSelectedVendors((prev) =>
      prev.includes(vendor)
        ? prev.filter((v) => v !== vendor)
        : [...prev, vendor],
    );
  };

  return (
    <aside className="w-64 bg-white shadow-lg p-4 min-h-screen">
      <div className="mb-6">
        <h3 className="font-semibold mb-3">Preisspanne</h3>
        <div className="space-y-2">
          <input
            type="range"
            min="0"
            max="100"
            value={priceRange.max}
            onChange={(e) =>
              setPriceRange((prev) => ({
                ...prev,
                max: Number(e.target.value),
              }))
            }
            className="w-full"
          />
          <div className="flex justify-between text-sm text-gray-600">
            <span>{priceRange.min}€</span>
            <span>{priceRange.max}€</span>
          </div>
        </div>
      </div>

      <div className="mb-6">
        <h3 className="font-semibold mb-3">Kategorien</h3>
        <div className="space-y-2">
          {categories.map((category) => (
            <label key={category} className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={selectedCategories.includes(category)}
                onChange={() => handleCategoryChange(category)}
                className="rounded text-purple-600 focus:ring-purple-500"
              />
              <span className="text-sm">{category}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="mb-6">
        <h3 className="font-semibold mb-3">Anbieter</h3>
        <div className="space-y-2">
          {vendors.map((vendor) => (
            <label key={vendor} className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={selectedVendors.includes(vendor)}
                onChange={() => handleVendorChange(vendor)}
                className="rounded text-purple-600 focus:ring-purple-500"
              />
              <span className="text-sm">{vendor}</span>
            </label>
          ))}
        </div>
      </div>

      <button
        onClick={() => {
          setSelectedCategories([]);
          setSelectedVendors([]);
          setPriceRange({ min: 0, max: 100 });
        }}
        className="w-full py-2 px-4 bg-gray-100 text-gray-700 rounded hover:bg-gray-200 transition-colors"
      >
        Filter zurücksetzen
      </button>
    </aside>
  );
}

export default Sidebar;
