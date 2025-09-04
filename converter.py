import json
import argparse
import io
from Bio.PDB import MMCIFParser, PDBIO

def convert_mmcif_in_json_to_pdb(json_path, pdb_path):
    """
    Extracts an mmCIF string from a JSON file and converts it to PDB format.
    """
    print(f"▶️  Reading JSON file: {json_path}")
    
    # --- Step 1: Load the JSON and extract the mmCIF string ---
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        cif_string = data['structures'][0]['structure']
        print("✅ Successfully extracted mmCIF data from JSON.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{json_path}' was not found.")
        return
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"❌ Error: Could not read or parse the JSON file. It may be invalid or have an unexpected structure.")
        print(f"   Details: {e}")
        return

    # --- Step 2: Use Biopython to parse the mmCIF string and write to PDB ---
    try:
        print("🔄 Converting mmCIF data to PDB format...")
        
        cif_io = io.StringIO(cif_string)
        
        parser = MMCIFParser()
        
        structure = parser.get_structure("MODEL", cif_io)
        
        pdb_io = PDBIO()
        pdb_io.set_structure(structure)
        
        pdb_io.save(pdb_path)
        
        print(f"✅ Success! PDB file created at '{pdb_path}'.")

    except Exception as e:
        print(f"❌ An error occurred during the Biopython conversion process.")
        print(f"   Details: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts a JSON-wrapped mmCIF file to PDB format."
    )
    parser.add_argument(
        "json_input", 
        help="Path to the input JSON file containing the mmCIF data."
    )
    parser.add_argument(
        "pdb_output", 
        help="Path for the output PDB file."
    )
    
    args = parser.parse_args()
    
    convert_mmcif_in_json_to_pdb(args.json_input, args.pdb_output)
