def load_containers(capacity, containers):
    current_capacity = 0
    loaded_containers=[]
    test_containers=[]
    containers
    containers=sorted(containers)
    j=1
    count=1
    max_containers=0

    for i in containers:
        loaded_containers.append(i)

        for j in containers:
            if current_capacity + cont <= capacity:
                count+=1
                loaded_containers.append(j)
        
        if(count>max):
            max=count
            test_containers=loaded_containers

        count=0
    return test_containers,max_containers


capacity =input("lütfen gemi kapasite giriniz:")
cont= input("konteyner ağırlıklarını arasına boşluk koyarak giriniz")
containers_split=cont.split(' ')
load_containers(capacity, containers_split)




