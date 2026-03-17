#!/usr/bin/env python3
"""
Query Template

This template provides common query patterns for Senzing.
Customize for your specific use cases.

Usage:
    python query_template.py
"""

import json
from typing import Dict, List, Optional
from senzing import G2Engine

# Configuration
CONFIG_FILE = "config/senzing_config.json"


class SenzingQuery:
    """Query interface for Senzing"""
    
    def __init__(self, config_file: str = CONFIG_FILE):
        """Initialize Senzing engine"""
        with open(config_file) as f:
            self.config = json.load(f)
        
        self.engine = G2Engine()
        self.engine.init("QueryApp", json.dumps(self.config), False)
    
    def get_entity_by_record(self, data_source: str, record_id: str) -> Optional[Dict]:
        """
        Get entity for a specific record.
        
        Args:
            data_source: Data source code (e.g., "CRM")
            record_id: Record ID from source system
        
        Returns:
            Entity dictionary or None if not found
        """
        try:
            entity_json = self.engine.getEntityByRecordID(data_source, record_id)
            return json.loads(entity_json)
        except Exception as e:
            print(f"Error getting entity: {e}")
            return None
    
    def get_entity_by_id(self, entity_id: int) -> Optional[Dict]:
        """
        Get entity by Senzing entity ID.
        
        Args:
            entity_id: Senzing entity ID
        
        Returns:
            Entity dictionary or None if not found
        """
        try:
            entity_json = self.engine.getEntityByEntityID(entity_id)
            return json.loads(entity_json)
        except Exception as e:
            print(f"Error getting entity: {e}")
            return None
    
    def search_by_attributes(self, name: str = None, email: str = None, 
                            phone: str = None, address: str = None) -> List[Dict]:
        """
        Search for entities by attributes.
        
        Args:
            name: Full name
            email: Email address
            phone: Phone number
            address: Full address
        
        Returns:
            List of matching entities
        """
        # Build search criteria
        search_criteria = {}
        
        if name:
            search_criteria["NAME_FULL"] = name
        if email:
            search_criteria["EMAIL_ADDRESS"] = email
        if phone:
            search_criteria["PHONE_NUMBER"] = phone
        if address:
            search_criteria["ADDR_FULL"] = address
        
        if not search_criteria:
            print("Error: Must provide at least one search criterion")
            return []
        
        try:
            result_json = self.engine.searchByAttributes(json.dumps(search_criteria))
            result = json.loads(result_json)
            return result.get('RESOLVED_ENTITIES', [])
        except Exception as e:
            print(f"Error searching: {e}")
            return []
    
    def find_duplicates_in_source(self, data_source: str) -> List[Dict]:
        """
        Find duplicate records within a single data source.
        
        Args:
            data_source: Data source code
        
        Returns:
            List of entities with multiple records from same source
        """
        duplicates = []
        
        try:
            export_handle = self.engine.exportJSONEntityReport(0)
            
            while True:
                entity_json = self.engine.fetchNext(export_handle)
                if not entity_json:
                    break
                
                entity = json.loads(entity_json)
                records = entity['RESOLVED_ENTITY']['RECORDS']
                
                # Count records from this data source
                source_records = [r for r in records if r['DATA_SOURCE'] == data_source]
                
                if len(source_records) > 1:
                    duplicates.append({
                        'entity_id': entity['RESOLVED_ENTITY']['ENTITY_ID'],
                        'name': entity['RESOLVED_ENTITY']['ENTITY_NAME'],
                        'record_count': len(source_records),
                        'record_ids': [r['RECORD_ID'] for r in source_records]
                    })
            
            self.engine.closeExport(export_handle)
        
        except Exception as e:
            print(f"Error finding duplicates: {e}")
        
        return duplicates
    
    def find_cross_source_matches(self) -> List[Dict]:
        """
        Find entities with records from multiple data sources.
        
        Returns:
            List of entities with cross-source matches
        """
        matches = []
        
        try:
            export_handle = self.engine.exportJSONEntityReport(0)
            
            while True:
                entity_json = self.engine.fetchNext(export_handle)
                if not entity_json:
                    break
                
                entity = json.loads(entity_json)
                records = entity['RESOLVED_ENTITY']['RECORDS']
                
                # Get unique data sources
                sources = set(r['DATA_SOURCE'] for r in records)
                
                if len(sources) > 1:
                    matches.append({
                        'entity_id': entity['RESOLVED_ENTITY']['ENTITY_ID'],
                        'name': entity['RESOLVED_ENTITY']['ENTITY_NAME'],
                        'sources': list(sources),
                        'record_count': len(records)
                    })
            
            self.engine.closeExport(export_handle)
        
        except Exception as e:
            print(f"Error finding matches: {e}")
        
        return matches
    
    def get_statistics(self) -> Dict:
        """
        Get database statistics.
        
        Returns:
            Statistics dictionary
        """
        try:
            stats_json = self.engine.stats()
            return json.loads(stats_json)
        except Exception as e:
            print(f"Error getting statistics: {e}")
            return {}
    
    def print_entity(self, entity: Dict):
        """Pretty print an entity"""
        if not entity:
            print("No entity found")
            return
        
        resolved = entity['RESOLVED_ENTITY']
        
        print(f"\n{'='*60}")
        print(f"Entity ID: {resolved['ENTITY_ID']}")
        print(f"Name: {resolved['ENTITY_NAME']}")
        print(f"{'='*60}")
        
        # Records
        print(f"\nRecords ({len(resolved['RECORDS'])}):")
        for record in resolved['RECORDS']:
            print(f"  - {record['DATA_SOURCE']}: {record['RECORD_ID']}")
        
        # Contact info
        if 'PHONE' in resolved:
            print(f"\nPhone Numbers:")
            for phone in resolved['PHONE']:
                print(f"  - {phone['PHONE_NUMBER']}")
        
        if 'EMAIL' in resolved:
            print(f"\nEmail Addresses:")
            for email in resolved['EMAIL']:
                print(f"  - {email['EMAIL_ADDRESS']}")
        
        if 'ADDRESS' in resolved:
            print(f"\nAddresses:")
            for addr in resolved['ADDRESS']:
                print(f"  - {addr.get('ADDR_FULL', 'N/A')}")
    
    def cleanup(self):
        """Clean up resources"""
        self.engine.destroy()


def example_queries():
    """Example usage of query functions"""
    
    query = SenzingQuery()
    
    try:
        print("="*60)
        print("SENZING QUERY EXAMPLES")
        print("="*60)
        
        # Example 1: Get entity by record
        print("\n1. Get entity by record ID:")
        entity = query.get_entity_by_record("CRM", "CRM-001")
        if entity:
            query.print_entity(entity)
        
        # Example 2: Search by name
        print("\n2. Search by name:")
        results = query.search_by_attributes(name="John Smith")
        print(f"Found {len(results)} matches")
        for i, result in enumerate(results[:5], 1):
            print(f"  {i}. Entity {result['ENTITY']['ENTITY_ID']}: {result['ENTITY']['ENTITY_NAME']}")
        
        # Example 3: Find duplicates
        print("\n3. Find duplicates in CRM:")
        duplicates = query.find_duplicates_in_source("CRM")
        print(f"Found {len(duplicates)} duplicate entities")
        for dup in duplicates[:5]:
            print(f"  - Entity {dup['entity_id']}: {dup['name']} ({dup['record_count']} records)")
        
        # Example 4: Find cross-source matches
        print("\n4. Find cross-source matches:")
        matches = query.find_cross_source_matches()
        print(f"Found {len(matches)} entities with multiple sources")
        for match in matches[:5]:
            print(f"  - Entity {match['entity_id']}: {match['name']} (sources: {', '.join(match['sources'])})")
        
        # Example 5: Get statistics
        print("\n5. Database statistics:")
        stats = query.get_statistics()
        if stats:
            print(f"  Total records: {stats.get('totalRecords', 'N/A')}")
            print(f"  Total entities: {stats.get('totalEntities', 'N/A')}")
    
    finally:
        query.cleanup()


if __name__ == '__main__':
    example_queries()
