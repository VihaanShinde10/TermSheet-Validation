#!/usr/bin/env python3
"""
Reference File Manager
Handles loading and managing reference files for validation
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path

class ReferenceFileManager:
    """Manages reference files for validation"""
    
    def __init__(self):
        self.reference_dir = Path("../uploads/reference")
        self.samples_dir = Path("../uploads/samples")
        self._validation_rules = None
        self._compliance_reference = None
    
    async def load_validation_rules(self) -> Dict[str, Any]:
        """Load validation rules from reference file"""
        if self._validation_rules is None:
            try:
                rules_file = self.reference_dir / "validation_rules_reference.json"
                if rules_file.exists():
                    with open(rules_file, 'r') as f:
                        self._validation_rules = json.load(f)
                else:
                    # Default validation rules if file doesn't exist
                    self._validation_rules = {
                        "validation_rules": {
                            "notional_amount": {
                                "tolerance": 0.05,
                                "critical_threshold": 0.1,
                                "data_type": "numeric"
                            },
                            "interest_rate": {
                                "tolerance": 0.25,
                                "critical_threshold": 0.5,
                                "data_type": "numeric"
                            }
                        },
                        "risk_scoring": {
                            "critical_discrepancy": 25,
                            "minor_discrepancy": 10,
                            "warning": 5,
                            "max_score": 100
                        }
                    }
            except Exception as e:
                print(f"Error loading validation rules: {e}")
                self._validation_rules = {"validation_rules": {}, "risk_scoring": {}}
        
        return self._validation_rules

# Global instance
reference_manager = ReferenceFileManager()
