from backend.app.agents.pharmacist_agent import run_pharmacist_agent


def test_pharmacist():

    # Test Case 1: Safe medication
    data1 = {
        "medications": ["Crocin"],
        "conditions": []
    }

    # Test Case 2: Drug interaction
    data2 = {
        "medications": ["Brufen", "Aspirin"],
        "conditions": []
    }

    # Test Case 3: Contraindication
    data3 = {
        "medications": ["Brufen"],
        "conditions": ["peptic_ulcer"]
    }

    print("Test 1:", run_pharmacist_agent(data1))
    print("Test 2:", run_pharmacist_agent(data2))
    print("Test 3:", run_pharmacist_agent(data3))


if __name__ == "__main__":
    test_pharmacist()