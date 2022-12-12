from . import real_data_deepface
# db_path = 'D:/JMM/05 django/attendance/media/'
db_path = '/JMM/05 django/attendance/media/'
# db_path = 'D:/JMM/00 IMAGES/Hurair/'
metrics = ["cosine", "euclidean", "euclidean_l2"]



def stream(db_path = db_path, model_name ='VGG-Face', detector_backend = 'opencv', distance_metric = 'cosine', enable_face_analysis = True, source = 0, time_threshold = 5, frame_threshold = 5):

	if time_threshold < 1:
		raise ValueError("time_threshold must be greater than the value 1 but you passed "+str(time_threshold))

	if frame_threshold < 1:
		raise ValueError("frame_threshold must be greater than the value 1 but you passed "+str(frame_threshold))

	name_and_date = real_data_deepface.analysis(db_path, model_name, detector_backend, distance_metric, enable_face_analysis
						, source = source, time_threshold = time_threshold, frame_threshold = frame_threshold)
 
    
	return name_and_date
 




