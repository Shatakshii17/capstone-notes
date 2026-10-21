cat >> test_plan.md << 'EOF'

Goal: tell titanium from Inconel fasteners with at least 99% certainty.

Tests:
1. Unit: check that each sensor reading is read and converted correctly.
2. Integration: run the CSV file through the classifier and check the output.
3. System: test the full setup once the hardware arrives.
4. Acceptance: check results against the sponsor requirement.
EOF
