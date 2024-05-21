import { Injectable } from '@nestjs/common';
import bcrypt from 'bcrypt';
import { SALT_ROUNDS } from 'src/users/constants';
import { faker } from '@faker-js/faker';
import { User } from 'src/users/types';

@Injectable()
export class UsersService {
  constructor() {}

  async registerUser(
    email: string,
    password: string,
  ): Promise<User | undefined> {
    try {
      const salt = await bcrypt.genSalt(SALT_ROUNDS);
      const hash = await bcrypt.hash(password, salt);
      const username = faker.internet.userName();
      return undefined;
    } catch (error) {
      console.log('Error registering user:', error);
      return undefined;
    }
  }

  async findUserByUsername(username: string) {
    return undefined;
  }

  async findUserByEmail(email: string) {
    return undefined;
  }

  async findUserById(id: number) {
    return undefined;
  }
}
