import json
import os
import re

def test_snippets():
    file_path = "serkom-laravel.code-snippets"
    assert os.path.exists(file_path), f"File {file_path} not found"
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"Total snippets loaded: {len(data)}")
    assert len(data) >= 54, f"Expected >= 54 snippets, got {len(data)}"
    
    # Required prefixes from task specification
    required_prefixes = [
        "mig-users", "mig-tickets", "mig-orders-ticket", "mig-details-ticket",
        "mig-foods", "mig-orders-food", "mig-details-food",
        "model-user", "model-ticket", "model-order-ticket", "model-detail-ticket",
        "model-food", "model-order-food", "model-detail-food",
        "ctrl-ticket", "ctrl-user", "ctrl-order-ticket", "ctrl-customer-booking",
        "ctrl-food", "ctrl-order-food", "ctrl-customer-food", "ctrl-auth-redirect",
        "mid-isadmin",
        "seeder-ticket", "seeder-database-ticket", "seeder-food", "seeder-database-food",
        "route-ticket-complete", "route-food-complete",
        "blade-ticket-index", "blade-ticket-create", "blade-ticket-edit",
        "blade-user-index", "blade-user-create", "blade-user-edit",
        "blade-admin-dashboard-rekap", "blade-admin-orders-print",
        "blade-customer-catalog", "blade-customer-booking", "blade-customer-my-tickets", "blade-customer-e-ticket",
        "blade-food-index", "blade-food-create", "blade-food-edit",
        "blade-resto-orders-index", "blade-resto-menu-catalog", "blade-resto-checkout",
        "blade-master-layout", "blade-flash-messages",
        "sql-crud-tickets", "sql-rekap-omset", "sql-crud-foods",
        "artisan-serkom-setup", "artisan-commands"
    ]
    
    # Required scope languages from specification
    required_scope_langs = {"php", "blade", "html", "sql", "json", "shellscript"}
    
    found_prefixes = set()
    for name, item in data.items():
        assert "prefix" in item, f"Missing prefix in {name}"
        assert "body" in item, f"Missing body in {name}"
        assert "description" in item, f"Missing description in {name}"
        assert isinstance(item["body"], list), f"Body must be a list in {name}"
        assert len(item["body"]) > 0, f"Body cannot be empty in {name}"
        
        prefix = item["prefix"]
        found_prefixes.add(prefix)
        
        # Verify scope coverage
        if "scope" in item and item["scope"]:
            scopes = set(s.strip() for s in item["scope"].split(","))
            missing_scopes = required_scope_langs - scopes
            assert len(missing_scopes) == 0, f"Snippet '{name}' ({prefix}) missing required scopes: {missing_scopes}"
        
        # Verify tab stops presence
        body_text = "\n".join(item["body"])
        has_tabstop = bool(re.search(r'\$[0-9]+|\$\{[0-9]+:[^}]+\}', body_text))
        assert has_tabstop, f"Snippet '{name}' ({prefix}) MUST have at least one tabstop ($1, $2, $0, etc.)!"
        
        # Verify variable escaping:
        # In VS Code snippet body, an unescaped $ followed by a letter/underscore:
        # Pattern: (?<!\\)\$([a-zA-Z_])
        # If this matches, it means there is an unescaped PHP variable that VS Code will swallow!
        for line_idx, line in enumerate(item["body"]):
            unescaped_vars = re.findall(r'(?<!\\)\$([a-zA-Z_][a-zA-Z0-9_]*)', line)
            if unescaped_vars:
                raise AssertionError(
                    f"Snippet '{name}' (prefix: '{prefix}') line {line_idx+1} has UNESCAPED variable(s): {unescaped_vars}\nLine content: {line}"
                )
    
    # Check that all required prefixes exist
    missing = [p for p in required_prefixes if p not in found_prefixes]
    assert len(missing) == 0, f"Missing prefixes: {missing}"
    
    print("SUCCESS: All 54 required prefixes present, 100% have tab stops, zero unescaped variables found!")
    print(f"Verified prefixes count: {len(found_prefixes)}")

if __name__ == "__main__":
    test_snippets()
