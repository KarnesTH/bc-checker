export interface Price {
  id: number;
  price: number;
  unit: string;
  vendor: string;
  url?: string;
  timestamp: string;
}

export interface Product {
  id: number;
  name: string;
  sku: string;
  category: string;
  prices: Price[];
}
