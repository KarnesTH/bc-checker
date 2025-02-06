import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface FilterState {
  selectedCategories: string[];
  selectedVendors: string[];
  priceRange: {
    min: number;
    max: number;
  };
}

const initialState: FilterState = {
  selectedCategories: [],
  selectedVendors: [],
  priceRange: {
    min: 0,
    max: 100,
  },
};

const filterSlice = createSlice({
  name: "filter",
  initialState,
  reducers: {
    setCategories: (state, action: PayloadAction<string[]>) => {
      state.selectedCategories = action.payload;
    },
    setVendors: (state, action: PayloadAction<string[]>) => {
      state.selectedVendors = action.payload;
    },
    setPriceRange: (
      state,
      action: PayloadAction<{ min: number; max: number }>,
    ) => {
      state.priceRange = action.payload;
    },
    resetFilter: () => {
      return initialState;
    },
  },
});

export const { setCategories, setVendors, setPriceRange, resetFilter } =
  filterSlice.actions;
export default filterSlice.reducer;
