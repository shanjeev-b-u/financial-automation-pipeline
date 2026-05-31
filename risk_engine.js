// Process each row one by one safely
return items.map(item => {
    const itemData = item.json;

    const entry = parseFloat(itemData["Entry Price"]) || 0;
    const quantity = parseInt(itemData["Quantity"]) || 0;

    // Core Calculations
    const stop_loss = entry * 0.97; // 3% risk protection
    const risk_per_share = entry - stop_loss;
    const target = entry + (risk_per_share * 2); // 1:2 Risk-Reward
    const capital_needed = entry * quantity;

    return {
        json: {
            ...itemData,
            target: Math.round(target * 100) / 100,
            stop_loss: Math.round(stop_loss * 100) / 100,
            capital_needed: Math.round(capital_needed)
        }
    };
});
