import os

YAML_EXT = "yaml"

def get_filename():
        return os.path.basename(__file__)

def get_yaml_output_filename(input_fn):
        basename = os.path.basename(input_fn)
        basename, fst_ext = os.path.splitext(basename)
        name, snd_ext = os.path.splitext(basename)
        
        if fst_ext == ".py" and snd_ext == ".tpl":
            return f"{name}.{YAML_EXT}"
        else:
            raise ValueError(f'${input_fn} is invalid format (filename.tpl.py)')
            return name
        
