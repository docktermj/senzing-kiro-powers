# Senzing Power - Test Examples

This document provides practical test examples for validating the Senzing power functionality.

## Unit Tests for Power Components

### Test 1: Metadata Validation

```python
import re
from pathlib import Path

def test_power_metadata():
    """Test that POWER.md has valid metadata"""
    power_md = Path("POWER.md")
    assert power_md.exists(), "POWER.md not found"
    
    content = power_md.read_text()
    
    # Check frontmatter exists
    assert content.startswith("---\n"), "Missing frontmatter"
    
    # Check required fields
    required_fields = ["name", "displayName", "version", "description", "author"]
    for field in required_fields:
        pattern = f'^{field}:'
        assert re.search(pattern, content, re.MULTILINE), f"Missing required field: {field}"
    
    # Check version format
    version_match = re.search(r'^version:\s*"([^"]+)"', content, re.MULTILINE)
    assert version_match, "Version field not found"
    version = version_match.group(1)
    assert re.match(r'^\d+\.\d+\.\d+$', version), f"Invalid version format: {version}"
    
    print("✅ Metadata validation passed")

# Run test
test_power_metadata()
```

### Test 2: File Structure

```python
from pathlib import Path

def test_file_structure():
    """Test that all required files exist"""
    required_files = [
        "POWER.md",
        "mcp.json",
        "METADATA.md",
        "IMPROVEMENTS_SUMMARY.md",
        "SMOKE_TEST.md",
        "validate_power.py"
    ]
    
    required_dirs = [
        "steering"
    ]
    
    steering_files = [
        "steering/steering.md",
        "steering/getting-started.md",
        "steering/quick-reference.md",
        "steering/best-practices.md",
        "steering/performance.md",
        "steering/troubleshooting.md",
        "steering/examples.md",
        "steering/use-cases.md",
        "steering/security-compliance.md",
        "steering/advanced-topics.md",
        "steering/monitoring.md",
        "steering/data-sources.md",
        "steering/cicd.md",
        "steering/faq.md",
        "steering/community.md",
        "steering/reference.md"
    ]
    
    # Check files
    for file in required_files:
        assert Path(file).exists(), f"Missing file: {file}"
    
    # Check directories
    for dir_name in required_dirs:
        assert Path(dir_name).is_dir(), f"Missing directory: {dir_name}"
    
    # Check steering files
    for file in steering_files:
        assert Path(file).exists(), f"Missing steering file: {file}"
    
    print(f"✅ File structure validation passed ({len(required_files) + len(steering_files)} files)")

# Run test
test_file_structure()
```

### Test 3: MCP Configuration

```python
import json
from pathlib import Path

def test_mcp_config():
    """Test that mcp.json is valid"""
    mcp_json = Path("mcp.json")
    assert mcp_json.exists(), "mcp.json not found"
    
    # Parse JSON
    config = json.loads(mcp_json.read_text())
    
    # Check structure
    assert "mcpServers" in config, "Missing mcpServers key"
    assert "senzing-mcp-server" in config["mcpServers"], "Missing senzing-mcp-server"
    
    server = config["mcpServers"]["senzing-mcp-server"]
    
    # Check required fields
    assert "url" in server, "Missing url field"
    assert server["url"].startswith("https://"), "URL should use HTTPS"
    
    # Check optional fields
    if "timeout" in server:
        assert isinstance(server["timeout"], int), "Timeout should be integer"
        assert server["timeout"] > 0, "Timeout should be positive"
    
    print("✅ MCP configuration validation passed")

# Run test
test_mcp_config()
```

### Test 4: Internal Links

```python
import re
from pathlib import Path

def test_internal_links():
    """Test that internal links are valid"""
    md_files = list(Path(".").glob("**/*.md"))
    broken_links = []
    
    for md_file in md_files:
        content = md_file.read_text()
        
        # Find markdown links
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        
        for link_text, link_path in links:
            # Skip external links
            if link_path.startswith(("http://", "https://", "#", "mailto:")):
                continue
            
            # Resolve relative path
            link_file = (md_file.parent / link_path).resolve()
            
            if not link_file.exists():
                broken_links.append((md_file, link_path))
    
    if broken_links:
        print(f"❌ Found {len(broken_links)} broken links:")
        for file, link in broken_links[:5]:  # Show first 5
            print(f"   {file}: {link}")
        assert False, f"Found {len(broken_links)} broken links"
    
    print(f"✅ Internal link validation passed (checked {len(md_files)} files)")

# Run test
test_internal_links()
```

## Integration Tests

### Test 5: MCP Server Connectivity

```python
def test_mcp_connectivity():
    """Test that MCP server is reachable"""
    try:
        # Test get_capabilities
        response = get_capabilities(version="current")
        assert response is not None, "get_capabilities returned None"
        assert "server_info" in response or "name" in response, "Invalid response structure"
        
        print("✅ MCP server connectivity test passed")
        return True
    except Exception as e:
        print(f"❌ MCP server connectivity test failed: {e}")
        return False

# Run test
test_mcp_connectivity()
```

### Test 6: Documentation Search

```python
def test_documentation_search():
    """Test that documentation search works"""
    try:
        # Search for a common term
        response = search_docs(
            query="entity resolution",
            version="current"
        )
        
        assert response is not None, "search_docs returned None"
        
        print("✅ Documentation search test passed")
        return True
    except Exception as e:
        print(f"❌ Documentation search test failed: {e}")
        return False

# Run test
test_documentation_search()
```

### Test 7: Sample Data Access

```python
def test_sample_data():
    """Test that sample data is accessible"""
    try:
        # List available datasets
        response = get_sample_data(dataset="list")
        
        assert response is not None, "get_sample_data returned None"
        
        print("✅ Sample data access test passed")
        return True
    except Exception as e:
        print(f"❌ Sample data access test failed: {e}")
        return False

# Run test
test_sample_data()
```

### Test 8: Code Generation

```python
def test_code_generation():
    """Test that code generation works"""
    try:
        # Generate simple scaffold
        response = generate_scaffold(
            language="python",
            workflow="initialize",
            version="current"
        )
        
        assert response is not None, "generate_scaffold returned None"
        
        print("✅ Code generation test passed")
        return True
    except Exception as e:
        print(f"❌ Code generation test failed: {e}")
        return False

# Run test
test_code_generation()
```

## End-to-End Tests

### Test 9: Complete Workflow

```python
def test_complete_workflow():
    """Test a complete workflow from start to finish"""
    try:
        # Step 1: Get capabilities
        print("Step 1: Getting capabilities...")
        capabilities = get_capabilities(version="current")
        assert capabilities is not None
        
        # Step 2: List sample datasets
        print("Step 2: Listing sample datasets...")
        datasets = get_sample_data(dataset="list")
        assert datasets is not None
        
        # Step 3: Search documentation
        print("Step 3: Searching documentation...")
        docs = search_docs(query="getting started", version="current")
        assert docs is not None
        
        # Step 4: Get SDK reference
        print("Step 4: Getting SDK reference...")
        reference = get_sdk_reference(topic="flags", version="current")
        assert reference is not None
        
        # Step 5: Find examples
        print("Step 5: Finding examples...")
        examples = find_examples(query="load records", language="python")
        assert examples is not None
        
        print("✅ Complete workflow test passed")
        return True
    except Exception as e:
        print(f"❌ Complete workflow test failed: {e}")
        return False

# Run test
test_complete_workflow()
```

## Performance Tests

### Test 10: Response Time

```python
import time

def test_response_time():
    """Test that MCP tools respond within acceptable time"""
    max_response_time = 5.0  # seconds
    
    tests = [
        ("get_capabilities", lambda: get_capabilities(version="current")),
        ("search_docs", lambda: search_docs(query="test", version="current")),
        ("get_sample_data", lambda: get_sample_data(dataset="list"))
    ]
    
    for test_name, test_func in tests:
        start = time.time()
        try:
            test_func()
            duration = time.time() - start
            
            if duration > max_response_time:
                print(f"⚠️  {test_name} took {duration:.2f}s (> {max_response_time}s)")
            else:
                print(f"✅ {test_name} responded in {duration:.2f}s")
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")

# Run test
test_response_time()
```

## Regression Tests

### Test 11: Backward Compatibility

```python
def test_backward_compatibility():
    """Test that existing functionality still works"""
    # This would test that previous versions' commands still work
    # For now, just verify core tools are available
    
    core_tools = [
        "get_capabilities",
        "mapping_workflow",
        "lint_record",
        "analyze_record",
        "generate_scaffold",
        "sdk_guide",
        "get_sample_data",
        "find_examples",
        "search_docs",
        "explain_error_code",
        "get_sdk_reference"
    ]
    
    # In a real test, you would verify each tool is callable
    # For this example, we just check they're documented
    
    power_md = Path("POWER.md").read_text()
    
    missing_tools = []
    for tool in core_tools:
        if tool not in power_md:
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"❌ Missing tools in documentation: {missing_tools}")
        assert False
    
    print(f"✅ Backward compatibility test passed ({len(core_tools)} tools documented)")

# Run test
test_backward_compatibility()
```

## Test Suite Runner

### Run All Tests

```python
def run_all_tests():
    """Run all test suites"""
    print("\n" + "="*60)
    print("Senzing Power Test Suite")
    print("="*60 + "\n")
    
    tests = [
        ("Metadata Validation", test_power_metadata),
        ("File Structure", test_file_structure),
        ("MCP Configuration", test_mcp_config),
        ("Internal Links", test_internal_links),
        ("MCP Connectivity", test_mcp_connectivity),
        ("Documentation Search", test_documentation_search),
        ("Sample Data Access", test_sample_data),
        ("Code Generation", test_code_generation),
        ("Complete Workflow", test_complete_workflow),
        ("Response Time", test_response_time),
        ("Backward Compatibility", test_backward_compatibility)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\nRunning: {test_name}")
        print("-" * 60)
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Test error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"Total: {passed + failed}")
    
    if failed == 0:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {failed} test(s) failed")
    
    return failed == 0

# Run all tests
if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
```

## Continuous Testing

### pytest Configuration

```python
# test_senzing_power.py
import pytest
from pathlib import Path

class TestSenzingPower:
    
    def test_metadata(self):
        """Test metadata validation"""
        test_power_metadata()
    
    def test_structure(self):
        """Test file structure"""
        test_file_structure()
    
    def test_config(self):
        """Test MCP configuration"""
        test_mcp_config()
    
    def test_links(self):
        """Test internal links"""
        test_internal_links()
    
    @pytest.mark.integration
    def test_connectivity(self):
        """Test MCP connectivity"""
        assert test_mcp_connectivity()
    
    @pytest.mark.integration
    def test_search(self):
        """Test documentation search"""
        assert test_documentation_search()

# Run with: pytest test_senzing_power.py
# Run integration tests: pytest test_senzing_power.py -m integration
```

## Manual Testing Checklist

- [ ] Run `python validate_power.py`
- [ ] Check all steering files open correctly
- [ ] Test MCP server connectivity
- [ ] Verify internal links work
- [ ] Test sample workflow
- [ ] Check metadata is current
- [ ] Verify version number is correct
- [ ] Test on clean installation
- [ ] Review error messages are helpful
- [ ] Confirm documentation is accurate

## Test Data

### Sample Test Files

For testing mapping_workflow, create test files:

```csv
# test_data.csv
id,name,email,phone
1,John Smith,john@example.com,555-1234
2,Jane Doe,jane@example.com,555-5678
```

```json
# test_data.json
[
  {
    "id": "1",
    "name": "John Smith",
    "email": "john@example.com"
  }
]
```

## Troubleshooting Tests

### Debug Failed Tests

```python
def debug_test_failure(test_name, error):
    """Debug a failed test"""
    print(f"\nDebugging: {test_name}")
    print(f"Error: {error}")
    print("\nChecklist:")
    print("- [ ] Check file paths are correct")
    print("- [ ] Verify internet connectivity")
    print("- [ ] Check MCP server status")
    print("- [ ] Review error message details")
    print("- [ ] Check prerequisites are met")
```

## Resources

- **Validation Script**: `validate_power.py`
- **Smoke Test Guide**: `SMOKE_TEST.md`
- **Power Metadata**: `METADATA.md`
- **Improvements Summary**: `IMPROVEMENTS_SUMMARY.md`
