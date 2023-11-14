import multiprocessing
from src import CreateDataSimulation

if __name__ == "__main__":
    with multiprocessing.Pool(processes=10) as pool:
        data_parte_1 = pool.apply_async(CreateDataSimulation.generar_data_csv_2,("data_parte_1_im.csv",0.2,1.0,0.00025,16,1,1,337500))
        data_parte_2 = pool.apply_async(generar_data_csv_2,("data_parte_2_im.csv",1.0,2.0,0.00025,16,1,1,337500))
        data_parte_3 = pool.apply_async(generar_data_csv_2,("data_parte_3_im.csv",2.0,3.0,0.00025,16,1,1,337500))
        data_parte_4 = pool.apply_async(generar_data_csv_2,("data_parte_4_im.csv",3.0,4.0,0.00025,16,1,1,337500))
        data_parte_5 = pool.apply_async(generar_data_csv_2,("data_parte_5_im.csv",4.0,5.0,0.00025,16,1,1,337500))
        data_parte_6 = pool.apply_async(generar_data_csv_2,("data_parte_6_im.csv",5.0,6.0,0.00025,16,1,1,337500))
        data_parte_7 = pool.apply_async(generar_data_csv_2,("data_parte_7_im.csv",6.0,7.0,0.00025,16,1,1,337500))
        data_parte_8 = pool.apply_async(generar_data_csv_2,("data_parte_8_im.csv",7.0,8.0,0.00025,16,1,1,337500))
        data_parte_9 = pool.apply_async(generar_data_csv_2,("data_parte_9_im.csv",8.0,9.0,0.00025,16,1,1,337500))
        data_parte_10 =pool.apply_async(generar_data_csv_2,("data_parte_10_im.csv",9.0,10.0,0.00025,16,1,1,337500))


        data_parte_1.get()
        data_parte_2.get() 
        data_parte_3.get() 
        data_parte_4.get() 
        data_parte_5.get() 
        data_parte_6.get() 
        data_parte_7.get() 
        data_parte_8.get() 
        data_parte_9.get() 
        data_parte_10.get()
        
        pool.close()
        pool.join()