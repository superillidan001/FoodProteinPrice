import streamlit as st

def calculate_protein_metrics():
    st.title("Food Protein Price Calculator")
    st.subheader("Calculate cost and nutrition for 100g of protein")
    
    with st.expander("How to use this calculator"):
        st.write("""
        1. Enter the food's total price (what you paid)
        2. Enter the total weight of the package
        3. Provide the serving size (as listed on nutrition label)
        4. Enter the protein, calories, carbs, and fat per serving
        5. See the results for 100g of protein from this food
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        price = st.number_input("Price of the food package ($)", min_value=0.0, step=0.01, value=5.99)
        unit = st.selectbox("Weight unit of package and serving size", ["grams (g)", "ounces (oz)", "pounds (lb)"])
        total_weight = st.number_input("Total weight of package", min_value=0.0, step=0.1, value=1.0)
        serving_size = st.number_input("Serving size (as on label)", min_value=0.0, step=0.1, value=4.0)
    
    with col2:
        protein_per_serving = st.number_input("Protein per serving (grams)", min_value=0.0, step=0.1, value=24.0)
        calories_per_serving = st.number_input("Calories per serving", min_value=0, step=1, value=120)
        carbs_per_serving = st.number_input("Carbs per serving (grams)", min_value=0.0, step=0.1, value=3.0)
        fat_per_serving = st.number_input("Fat per serving (grams)", min_value=0.0, step=0.1, value=1.5)
    
    # Convert all weights to grams
    if unit == "ounces (oz)":
        total_weight_grams = total_weight * 28.3495
        serving_size_grams = serving_size * 28.3495
    elif unit == "pounds (lb)":
        total_weight_grams = total_weight * 453.592
        serving_size_grams = serving_size * 453.592
    else:  # grams
        total_weight_grams = total_weight
        serving_size_grams = serving_size
    
    # Calculate metrics
    if protein_per_serving > 0 and serving_size_grams > 0 and total_weight_grams > 0:
        # Price calculations
        price_per_gram_protein = (price / total_weight_grams) * (serving_size_grams / protein_per_serving)
        price_per_100g_protein = price_per_gram_protein * 100
        
        # Nutrition calculations
        calories_per_100g_protein = (calories_per_serving / protein_per_serving) * 100
        carbs_per_100g_protein = (carbs_per_serving / protein_per_serving) * 100
        fat_per_100g_protein = (fat_per_serving / protein_per_serving) * 100
        
        # Package totals
        servings_per_package = total_weight_grams / serving_size_grams
        total_protein = protein_per_serving * servings_per_package
        total_calories = calories_per_serving * servings_per_package
        total_carbs = carbs_per_serving * servings_per_package
        total_fat = fat_per_serving * servings_per_package
        
        # Display results
        st.success("### Results for 100g of protein")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Price", f"${price_per_100g_protein:.2f}")
        with col2:
            st.metric("Calories", f"{calories_per_100g_protein:.0f}")
        with col3:
            st.metric("Carbs", f"{carbs_per_100g_protein:.1f}g")
        with col4:
            st.metric("Fat", f"{fat_per_100g_protein:.1f}g")
        
        # Additional info
        with st.expander("More details"):
            st.write(f"**Total protein in package:** {total_protein:.1f}g")
            st.write(f"**Total calories in package:** {total_calories:.0f}")
            st.write(f"**Total carbs in package:** {total_carbs:.1f}g")
            st.write(f"**Total fat in package:** {total_fat:.1f}g")
            st.write(f"**Protein density:** {100 * protein_per_serving / serving_size_grams:.1f}g protein per 100g food")
            
            # Conversion details (for debugging)
            st.write("\n**Conversion details:**")
            st.write(f"Package weight: {total_weight_grams:.1f}g")
            st.write(f"Serving size: {serving_size_grams:.1f}g")
    else:
        st.warning("Please enter positive values for protein, serving size, and package weight")

if __name__ == "__main__":
    calculate_protein_metrics()