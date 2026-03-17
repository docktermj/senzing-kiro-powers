#!/usr/bin/env python3
"""
Batch Loader Template

This template provides a starting point for loading Senzing JSON files into Senzing.
Includes error handling, progress tracking, and statistics.

Usage:
    python batch_loader_template.py data/transformed/your_data.jsonl
"""

import json
import sys
import time
from typing import Dict
from senzing import G2Engine

# Configuration
DATA_SOURCE = "YOUR_DATA_SOURCE"  # Change to your data source code
CONFIG_FILE = "config/senzing_config.json"  # Path to Senzing config
BATCH_SIZE = 1000  # Records per batch
PROGRESS_INTERVAL = 1000  # Show progress every N records


class BatchLoader:
    """Batch loader with error handling and statistics"""
    
    def __init__(self, config_file: str = CONFIG_FILE):
        """Initialize Senzing engine"""
        with open(config_file) as f:
            self.config = json.load(f)
        
        self.engine = G2Engine()
        self.engine.init("BatchLoader", json.dumps(self.config), False)
        
        self.stats = {
            'success': 0,
            'errors': 0,
            'start_time': None,
            'end_time': None
        }
        
        self.errors = []
    
    def load_record(self, record: Dict) -> bool:
        """
        Load a single record into Senzing.
        Returns True if successful, False if error.
        """
        try:
            self.engine.addRecord(
                record['DATA_SOURCE'],
                record['RECORD_ID'],
                json.dumps(record)
            )
            return True
        except Exception as e:
            self.errors.append({
                'record_id': record.get('RECORD_ID', 'UNKNOWN'),
                'error': str(e)
            })
            return False
    
    def load_file(self, input_file: str):
        """Load entire file"""
        print(f"{'='*60}")
        print(f"LOADING: {input_file}")
        print(f"{'='*60}")
        print(f"Data Source: {DATA_SOURCE}")
        print(f"Config: {CONFIG_FILE}")
        print()
        
        self.stats['start_time'] = time.time()
        
        with open(input_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    # Parse JSON
                    record = json.loads(line)
                    
                    # Load record
                    if self.load_record(record):
                        self.stats['success'] += 1
                    else:
                        self.stats['errors'] += 1
                    
                    # Progress indicator
                    if line_num % PROGRESS_INTERVAL == 0:
                        elapsed = time.time() - self.stats['start_time']
                        rate = line_num / elapsed
                        print(f"  Loaded {line_num:,} records ({rate:.1f} rec/sec)...")
                
                except json.JSONDecodeError as e:
                    self.stats['errors'] += 1
                    self.errors.append({
                        'line': line_num,
                        'error': f"JSON decode error: {e}"
                    })
                except Exception as e:
                    self.stats['errors'] += 1
                    self.errors.append({
                        'line': line_num,
                        'error': str(e)
                    })
        
        self.stats['end_time'] = time.time()
        self.print_summary()
    
    def print_summary(self):
        """Print loading statistics"""
        duration = self.stats['end_time'] - self.stats['start_time']
        total = self.stats['success'] + self.stats['errors']
        rate = self.stats['success'] / duration if duration > 0 else 0
        
        print()
        print("="*60)
        print("LOADING SUMMARY")
        print("="*60)
        print(f"Total Records: {total:,}")
        print(f"Success: {self.stats['success']:,}")
        print(f"Errors: {self.stats['errors']:,}")
        print(f"Duration: {duration:.1f} seconds")
        print(f"Rate: {rate:.1f} records/second")
        
        if self.stats['errors'] > 0:
            success_rate = (self.stats['success'] / total) * 100
            print(f"Success Rate: {success_rate:.2f}%")
            
            print(f"\nFirst 10 errors:")
            for error in self.errors[:10]:
                if 'record_id' in error:
                    print(f"  - Record {error['record_id']}: {error['error']}")
                else:
                    print(f"  - Line {error.get('line', '?')}: {error['error']}")
        
        if self.stats['errors'] == 0:
            print("\n✅ Loading completed successfully!")
        else:
            print(f"\n⚠️  Loading completed with {self.stats['errors']} errors")
    
    def cleanup(self):
        """Clean up resources"""
        self.engine.destroy()


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python batch_loader_template.py input.jsonl")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    loader = BatchLoader(CONFIG_FILE)
    try:
        loader.load_file(input_file)
    finally:
        loader.cleanup()


if __name__ == '__main__':
    main()
