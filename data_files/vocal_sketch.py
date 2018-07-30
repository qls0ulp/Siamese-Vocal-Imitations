import csv
import os

import utils.preprocessing as preprocessing
from data_files.generics import Datafiles
from utils.utils import get_dataset_dir


class VocalSketch(Datafiles):
    def __init__(self, version, recalculate_spectrograms=False):
        super().__init__(version, recalculate_spectrograms)

    @staticmethod
    def calculate_spectrograms():
        raise NotImplementedError


class VocalSketchV1(VocalSketch):
    def __init__(self, recalculate_spectrograms=False):
        super().__init__("vs1.0", recalculate_spectrograms)

    @staticmethod
    def calculate_spectrograms():
        """
        Calculates normalized imitation and reference spectrograms and saves them as .npy files.
        """
        data_dir = get_dataset_dir()
        imitation_path = os.path.join(data_dir, "vs1.0/vocal_imitations/included")
        reference_path = os.path.join(data_dir, "vs1.0/sound_recordings")

        imitation_paths = preprocessing.recursive_wav_paths(imitation_path)
        reference_paths = preprocessing.recursive_wav_paths(reference_path)

        reference_csv = os.path.join(data_dir, 'vs1.0', "sound_recordings.csv")
        imitation_csv = os.path.join(data_dir, 'vs1.0', "vocal_imitations.csv")

        reference_labels = {}
        with open(reference_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                path = os.path.join(reference_path, row['filename'])
                reference_labels[path] = {'label': row['sound_label'],
                                          'is_canonical': True}

        imitation_labels = {}
        with open(imitation_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                path = os.path.join(imitation_path, row['filename'])
                imitation_labels[path] = row['sound_label']

        preprocessing.calculate_spectrograms(imitation_paths, imitation_labels, 'imitations', 'vs1.0', preprocessing.imitation_spectrogram)
        preprocessing.calculate_spectrograms(reference_paths, reference_labels, 'references', 'vs1.0', preprocessing.reference_spectrogram)


class VocalSketchV2(VocalSketch):
    def __init__(self, recalculate_spectrograms=False):
        super().__init__("vs2.0", recalculate_spectrograms)

    @staticmethod
    def calculate_spectrograms():
        """
        Calculates normalized imitation and reference spectrograms and saves them as .npy files.
        """
        data_dir = get_dataset_dir()
        imitation_path_1 = os.path.join(data_dir, "vs2.0/vocal_imitations/included")
        imitation_path_2 = os.path.join(data_dir, "vs2.0/vocal_imitations_set2/included")
        reference_path = os.path.join(data_dir, "vs2.0/sound_recordings")

        imitation_paths = preprocessing.recursive_wav_paths(imitation_path_1) + preprocessing.recursive_wav_paths(imitation_path_2)
        reference_paths = preprocessing.recursive_wav_paths(reference_path)

        imitation_csv_1 = os.path.join(data_dir, 'vs2.0', "vocal_imitations.csv")
        imitation_csv_2 = os.path.join(data_dir, 'vs2.0', "vocal_imitaitons_set2.csv")  # not a typo, the CSV's name is misspelled
        reference_csv = os.path.join(data_dir, 'vs2.0', "sound_recordings.csv")

        reference_labels = {}
        with open(reference_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                path = os.path.join(reference_path, row['filename'])
                reference_labels[path] = {'label': row['sound_label'],
                                          'is_canonical': True}

        imitation_labels = {}
        with open(imitation_csv_1) as f:
            reader = csv.DictReader(f)
            for row in reader:
                path = os.path.join(imitation_path_1, row['filename'])
                imitation_labels[path] = row['sound_label']

        with open(imitation_csv_2) as f:
            reader = csv.DictReader(f)
            for row in reader:
                path = os.path.join(imitation_path_2, row['filename'])
                imitation_labels[path] = row['sound_label']

        preprocessing.calculate_spectrograms(imitation_paths, imitation_labels, 'imitations', 'vs2.0', preprocessing.imitation_spectrogram)
        preprocessing.calculate_spectrograms(reference_paths, reference_labels, 'references', 'vs2.0', preprocessing.reference_spectrogram)