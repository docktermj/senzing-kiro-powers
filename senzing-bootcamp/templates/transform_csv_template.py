#!/usr/bin/env python3
"""
CSV to Senzing JSON Transformation Template

This template provides a starting point for transforming CSV files to Senzing JSON format.
Customize the field mappings in transform_record() for your specific data source.

Usage:
    python transform_csv_template.py input.csv output.jsonl
"""

import json
import csv
import sys
from typing import Dict, Optional

# Configuration
DATA_SOURCE = "YOUR_DATA_SOURCE"  # Change this to your data source code
RECORD_TYPE = "PERSON"  # or "ORGANIZATION"

def transform_record(row: Dict[str, str]) -> Dict:
    """
    Transform a single CSV row to Senzing JSON format.
    
    Customize this function to map your CSV columns to Senzing attributes.
    
    Common Senzing attributes:
    - RECORD_ID: Unique identifier from source system
    - RECORD_TYPE: "PERSON" or "ORGANIZATION"
    - PRIMARY_NAME_LAST: Last name
    - PRIMARY_NAME_FIRST: First name
    - PRIMARY_NAME_MIDDLE: Middle name
    - PRIMARY_NAME_FULL: Full name (if not split)
    - EMAIL_ADDRESS: Email
    - PHONE_NUMBER: Phone
    - ADDR_FULL: Full address
    - ADDR_LINE1: Address line 1
    - ADDR_CITY: City
    - ADDR_STATE: State/province
    - ADDR_POSTAL_CODE: Postal/ZIP code
    - ADDR_COUNTRY: Country
    - DATE_OF_BIRTH: Birth date (YYYY-MM-DD)
    - SSN_NUMBER: Social Security Number
    - DRIVERS_LICENSE_NUMBER: Driver's license
    - PASSPORT_NUMBER: Passport number
    - NATIONAL_ID_NUMBER: National ID
    - TAX_ID_NUMBER: Tax ID (for organizations)
    - EMPLOYER_NAME: Employer name
    - ORGANIZATION_NAME: Organization name
    """
    
    # Basic template - customize these mappings
    senzing_record = {
        "DATA_SOURCE": DATA_SOURCE,
        "RECORD_ID": row.get('id', ''),  # Change 'id' to your ID column
        "RECORD_TYPE": RECORD_TYPE
    }
    
    # Name fields (for PERSON records)
    if RECORD_TYPE == "PERSON":
        if 'first_name' in row and 'last_name' in row:
            # If you have separate first/last names
            senzing_record["PRIMARY_NAME_FIRST"] = row['first_name']
            senzing_record["PRIMARY_NAME_LAST"] = row['last_name']
            if 'middle_name' in row and row['middle_name']:
                senzing_record["PRIMARY_NAME_MIDDLE"] = row['middle_name']
        elif 'full_name' in row:
            # If you have full name only
            senzing_record["PRIMARY_NAME_FULL"] = row['full_name']
    
    # Name fields (for ORGANIZATION records)
    if RECORD_TYPE == "ORGANIZATION":
        if 'company_name' in row:
            senzing_record["ORGANIZATION_NAME"] = row['company_name']
    
    # Contact information
    if 'email' in row and row['email']:
        senzing_record["EMAIL_ADDRESS"] = row['email']
    
    if 'phone' in row and row['phone']:
        senzing_record["PHONE_NUMBER"] = row['phone']
    
    # Address fields
    # Option 1: Full address in one field
    if 'address' in row and row['address']:
        senzing_record["ADDR_FULL"] = row['address']
    
    # Option 2: Structured address fields
    if 'address_line1' in row and row['address_line1']:
        senzing_record["ADDR_LINE1"] = row['address_line1']
    
    if 'city' in row and row['city']:
        senzing_record["ADDR_CITY"] = row['city']
    
    if 'state' in row and row['state']:
        senzing_record["ADDR_STATE"] = row['state']
    
    if 'zip' in row and row['zip']:
        senzing_record["ADDR_POSTAL_CODE"] = row['zip']
    
    if 'country' in row and row['country']:
        senzing_record["ADDR_COUNTRY"] = row['country']
    
    # Identifiers
    if 'ssn' in row and row['ssn']:
        senzing_record["SSN_NUMBER"] = row['ssn']
    
    if 'date_of_birth' in row and row['date_of_birth']:
        senzing_record["DATE_OF_BIRTH"] = row['date_of_birth']
    
    # Additional fields
    if 'employer' in row and row['employer']:
        senzing_record["EMPLOYER_NAME"] = row['employer']
    
    # Remove empty fields
    senzing_record = {k: v for k, v in senzing_record.items() if v}
    
    return senzing_record


def validate_record(record: Dict) -> Optional[str]:
    """
    Validate a Senzing record.
    Returns error message if invalid, None if valid.
    """
    # Must have DATA_SOURCE and RECORD_ID
    if not record.get('DATA_SOURCE'):
        return "Missing DATA_SOURCE"
    
    if not record.get('RECORD_ID'):
        return "Missing RECORD_ID"
    
    # Must have at least one name field
    name_fields = [
        'PRIMARY_NAME_FULL', 'PRIMARY_NAME_LAST', 'PRIMARY_NAME_FIRST',
        'ORGANIZATION_NAME'
    ]
    if not any(record.get(field) for field in name_fields):
        return "Missing name field (need at least one name)"
    
    return None


def transform_file(input_file: str, output_file: str):
    """Transform entire CSV file to Senzing JSON Lines format"""
    
    success_count = 0
    error_count = 0
    errors = []
    
    print(f"Transforming {input_file} -> {output_file}")
    print(f"Data Source: {DATA_SOURCE}")
    print(f"Record Type: {RECORD_TYPE}")
    print()
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        
        for line_num, row in enumerate(reader, 1):
            try:
                # Transform record
                senzing_record = transform_record(row)
                
                # Validate record
                error = validate_record(senzing_record)
                if error:
                    error_count += 1
                    errors.append(f"Line {line_num}: {error}")
                    continue
                
                # Write to output
                outfile.write(json.dumps(senzing_record) + '\n')
                success_count += 1
                
                # Progress indicator
                if line_num % 1000 == 0:
                    print(f"  Processed {line_num:,} records...")
            
            except Exception as e:
                error_count += 1
                errors.append(f"Line {line_num}: {str(e)}")
    
    # Print summary
    print()
    print("="*60)
    print("TRANSFORMATION SUMMARY")
    print("="*60)
    print(f"Success: {success_count:,} records")
    print(f"Errors: {error_count:,} records")
    
    if errors:
        print(f"\nFirst 10 errors:")
        for error in errors[:10]:
            print(f"  - {error}")
    
    if error_count == 0:
        print("\n✅ Transformation completed successfully!")
    else:
        print(f"\n⚠️  Transformation completed with {error_count} errors")
    
    return success_count, error_count


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python transform_csv_template.py input.csv output.jsonl")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    transform_file(input_file, output_file)
