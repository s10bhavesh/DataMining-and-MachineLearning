function [dst]=dtw2(s1,s2)
lr=length(s1);
lc=length(s2);
%% Calculation of cost matrix
cost_mat=zeros(lr,lc);
acc_cost_mat=cost_mat;
for i=1:lr
    for j=1:lc
        cost_mat(i,j)=norm((s1(i,:)-s2(j,:)),1);
    end
end
%% Calculation of accumulated cost matrix
for i=1:lr
    acc_cost_mat(i,1)=sum(cost_mat(1:i,1));
end
for j=1:lc
    acc_cost_mat(1,j)=sum(cost_mat(1,1:j));
end
for i=2:lr
    for j=2:lc
        t=[acc_cost_mat(i-1,j-1) acc_cost_mat(i,j-1) acc_cost_mat(i-1,j)];
        acc_cost_mat(i,j)=cost_mat(i,j)+min(t);
    end
end
%% Finding DTW path
[dpath]=dtw_path(acc_cost_mat);
lng=length(dpath);
dtw_cost=zeros(lng,1);
for p=1:lng
    dtw_cost(p,1) = cost_mat(dpath(1,p),dpath(2,p));
end
dst=acc_cost_mat(lr,lc)./lng;
